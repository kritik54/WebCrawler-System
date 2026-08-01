CREATE DATABASE WebCrawlerDB;
USE WebCrawlerDB;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE SeedURLs (
    seed_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    url VARCHAR(255) NOT NULL,
    priority INT DEFAULT 1,
    status VARCHAR(20),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE CrawlQueue (
    queue_id INT AUTO_INCREMENT PRIMARY KEY,
    seed_id INT,
    url VARCHAR(255),
    priority INT,
    status VARCHAR(20),
    queued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (seed_id) REFERENCES SeedURLs(seed_id)
);

CREATE TABLE CrawledPages (
    page_id INT AUTO_INCREMENT PRIMARY KEY,
    queue_id INT,
    page_url VARCHAR(255),
    title VARCHAR(255),
    html_content LONGTEXT,
    crawl_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    hash_value VARCHAR(255),
    FOREIGN KEY (queue_id) REFERENCES CrawlQueue(queue_id)
);

CREATE TABLE IndexedJobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    page_id INT,
    job_title VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(255),
    description TEXT,
    deadline DATE,
    source_url VARCHAR(255),
    indexed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (page_id) REFERENCES CrawledPages(page_id)
);

CREATE TABLE CrawlLogs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    page_id INT,
    status VARCHAR(50),
    response_code INT,
    message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (page_id) REFERENCES CrawledPages(page_id)
);

CREATE TABLE SearchHistory (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    job_id INT,
    search_keyword VARCHAR(255),
    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (job_id) REFERENCES IndexedJobs(job_id)
);