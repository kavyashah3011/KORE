"""
KORE Vector Memory System
-------------------------

Vector memory for storing and retrieving agent outputs using Qdrant.

Features
• Store research outputs
• Store task results
• Retrieve relevant context
• Semantic search for agents

Dependencies:
pip install qdrant-client sentence-transformers
"""

from typing import List, Dict, Any
from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

from sentence_transformers import SentenceTransformer


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

COLLECTION_NAME = "kore_memory"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
VECTOR_SIZE = 384


# ---------------------------------------------------------
# Vector Memory Class
# ---------------------------------------------------------

class VectorMemory:
    """
    Vector memory manager for KORE agents.
    Handles storing and retrieving semantic information.
    """

    def __init__(self, host: str = "localhost", port: int = 6333):

        self.client = QdrantClient(host=host, port=port)

        self.embedder = SentenceTransformer(EMBEDDING_MODEL)

        self._init_collection()

    # -----------------------------------------------------

    def _init_collection(self):
        """Create Qdrant collection if it doesn't exist."""

        collections = self.client.get_collections().collections
        names = [c.name for c in collections]

        if COLLECTION_NAME not in names:

            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,
                    distance=Distance.COSINE
                )
            )

    # -----------------------------------------------------

    def _embed(self, text: str) -> List[float]:
        """Convert text into embedding vector."""

        return self.embedder.encode(text).tolist()

    # -----------------------------------------------------

    def store(
        self,
        text: str,
        metadata: Dict[str, Any]
    ):
        """
        Store memory entry.

        metadata example:
        {
            "agent": "researcher",
            "type": "research_output",
            "task": "AI frameworks research"
        }
        """

        vector = self._embed(text)

        point = PointStruct(
            id=str(uuid4()),
            vector=vector,
            payload={
                "text": text,
                **metadata
            }
        )

        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=[point]
        )

    # -----------------------------------------------------

    def search(
        self,
        query: str,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant memory entries.
        """

        vector = self._embed(query)

        results = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=vector,
            limit=limit
        )

        memories = []

        for r in results:
            payload = r.payload
            payload["score"] = r.score
            memories.append(payload)

        return memories

    # -----------------------------------------------------

    def store_task_result(
        self,
        task_name: str,
        result: str,
        agent: str
    ):
        """Convenience function for saving task outputs."""

        self.store(
            text=result,
            metadata={
                "type": "task_result",
                "task": task_name,
                "agent": agent
            }
        )

    # -----------------------------------------------------

    def store_research(
        self,
        topic: str,
        research_output: str
    ):
        """Convenience function for storing research."""

        self.store(
            text=research_output,
            metadata={
                "type": "research",
                "topic": topic,
                "agent": "researcher"
            }
        )

    # -----------------------------------------------------

    def get_context(
        self,
        query: str,
        limit: int = 5
    ) -> str:
        """
        Retrieve relevant memory and combine as context
        for LLM agents.
        """

        results = self.search(query, limit)

        context_blocks = []

        for r in results:
            context_blocks.append(r["text"])

        return "\n\n".join(context_blocks)