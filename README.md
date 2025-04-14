# Chat With PDF - Generative AI Application
## Built Using Amazon Bedrock, Langchain, Python, Docker, Amazon S3

## Introduction
Welcome to my Chat With PDF application! In this project, I’ve combined several powerful technologies to build a Generative AI-powered Chatbot that can understand and interact with PDF documents. The system processes PDF files and enables users to query them for information in a conversational manner. It uses a combination of Amazon Bedrock, Langchain, FAISS, Docker, and Streamlit to ensure that responses are contextually relevant, generated through Retrieval-Augmented Generation (RAG) techniques.

This application serves as a demonstration of how Generative AI and Document Processing can be integrated into intelligent systems that allow for querying and interacting with PDF files stored in Amazon S3. The goal is to create an intelligent PDF chatbot system that can analyze, process, and answer questions based on the content from uploaded documents.


## Project Breakdown:
   The project is designed around two distinct yet interconnected applications:

### ADMIN Application: 
This allows administrators to upload PDFs, process them, and prepare the data for querying.
    - It breaks down the PDFs into smaller text chunks, creates embeddings using the Amazon Titan Embedding Model, and stores the resulting vectors in FAISS for efficient similarity search.
    - The embeddings are uploaded to an Amazon S3 bucket for centralized storage, from which the User Application can retrieve them.
   


### USER Application:
This application enables users to interact with the PDF documents and query them for specific information.
  - It starts by downloading the necessary FAISS index from the S3 bucket.
  - Users can submit questions, which are embedded into vectors using the same Amazon Titan Embedding Model.
  - The system then searches the FAISS index for the most relevant document chunks and combines them with the query to generate meaningful responses using Anthropic Claude.


## Key Technologies Used:
 - Amazon Bedrock: This is the core service that powers the large language models used in this project. I leveraged the Amazon Titan Embedding Model for creating vector embeddings and Anthropic Claude for generating intelligent responses.

 - Langchain: An essential part of the project that helps chain together multiple steps, such as converting the query into a vector, performing similarity search, and generating a response.

 - FAISS (Facebook AI Similarity Search): Used to efficiently index and search the document embeddings. FAISS allows for fast similarity search, which is key to providing relevant document chunks for each user query.
 - Docker: Docker provides a consistent and isolated environment for both the Admin and User applications. This ensures that the application can run seamlessly across different systems and environments.
 - Amazon S3: This is where the generated FAISS index is stored. The User Application retrieves the index from S3 to perform similarity search and get relevant results.


## Admin Application Workflow: 
The Admin Application plays a critical role in setting up the system by preparing the PDF documents for querying. Here’s how it works:
- Upload PDF: The administrator uploads a PDF document via a web interface.
- Text Chunking: The PDF content is processed and split into smaller chunks of text to improve the accuracy and performance of subsequent steps.

- Embedding Creation: Each text chunk is converted into a vector representation using the Amazon Titan Embedding Model. This step ensures that the textual content can be analyzed in a way that machines can process efficiently.

- FAISS Indexing: The generated vectors are indexed in FAISS, which allows for fast and efficient search operations later when the user submits queries.

- S3 Upload: The FAISS index is then uploaded to an Amazon S3 bucket. This serves as the cloud storage for the index, making it accessible to the User Application.



## User Application Workflow: 
Once the Admin Application has processed the PDFs and uploaded the vector index to S3, the User Application is ready to allow users to interact with the data:
- Index Download: The application downloads the FAISS index from S3 and sets it up for local use.

- User Query Handling: When a user submits a query, the application converts the query into a vector using the same Amazon Titan Embedding Model used in the Admin Application.

- Similarity Search: The system performs a similarity search on the FAISS index to retrieve the most relevant document chunks based on the query vector.

- Response Generation: Using Anthropic Claude, the relevant document chunks are combined with the user query to generate an accurate and context-aware response.



## Conclusion
The Chat With PDF application addresses the challenge of efficiently interacting with large PDF documents by enabling users to query them in a conversational manner. By leveraging state-of-the-art Generative AI and document processing technologies like Amazon Bedrock, Langchain, FAISS, and Amazon S3, this system allows users to quickly access relevant information from PDFs without manually searching through them. The combination of Retrieval-Augmented Generation (RAG) techniques ensures contextually accurate and insightful responses, significantly improving the way we interact with document-based data. This solution is particularly useful for businesses, researchers, and developers who need to process and query large volumes of text stored in PDF format, streamlining workflows and improving productivity.
