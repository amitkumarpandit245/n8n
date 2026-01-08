
CREATE TABLE documents (
    document_id VARCHAR(50) PRIMARY KEY,
    document_type VARCHAR(50),
    status VARCHAR(20),
    created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE document_data (
    id INT IDENTITY PRIMARY KEY,
    document_id VARCHAR(50),
    extracted_json NVARCHAR(MAX)
);
