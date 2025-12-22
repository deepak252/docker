-- =========================================================
-- MySQL 8.0
-- =========================================================

SET FOREIGN_KEY_CHECKS = 0;

-- =========================
-- 1. Countries
-- =========================
CREATE TABLE countries (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  iso_code CHAR(2) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- 2. Companies
-- =========================
CREATE TABLE companies (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  industry VARCHAR(100),
  country_id BIGINT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_companies_country
    FOREIGN KEY (country_id) REFERENCES countries(id)
) ENGINE=InnoDB;

-- =========================
-- 3. Products
-- =========================
CREATE TABLE products (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  company_id BIGINT NOT NULL,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  launch_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_products_company
    FOREIGN KEY (company_id) REFERENCES companies(id)
) ENGINE=InnoDB;

-- =========================
-- 4. Media Channels
-- =========================
CREATE TABLE media_channels (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  type VARCHAR(50), -- Paid / Organic
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- 5. Product Media (Images / Videos / PDFs)
-- =========================
CREATE TABLE product_media (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  product_id BIGINT NOT NULL,
  media_channel_id BIGINT NOT NULL,
  country_id BIGINT NOT NULL,
  media_type ENUM('IMAGE','VIDEO','PDF') NOT NULL,
  media_url TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_product_media_product
    FOREIGN KEY (product_id) REFERENCES products(id),

  CONSTRAINT fk_product_media_channel
    FOREIGN KEY (media_channel_id) REFERENCES media_channels(id),

  CONSTRAINT fk_product_media_country
    FOREIGN KEY (country_id) REFERENCES countries(id)
) ENGINE=InnoDB;

-- =========================
-- 6. Campaigns
-- =========================
CREATE TABLE campaigns (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  product_id BIGINT NOT NULL,
  media_channel_id BIGINT NOT NULL,
  country_id BIGINT NOT NULL,
  name VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE,
  budget DECIMAL(12,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_campaigns_product
    FOREIGN KEY (product_id) REFERENCES products(id),

  CONSTRAINT fk_campaigns_channel
    FOREIGN KEY (media_channel_id) REFERENCES media_channels(id),

  CONSTRAINT fk_campaigns_country
    FOREIGN KEY (country_id) REFERENCES countries(id)
) ENGINE=InnoDB;

-- =========================
-- 7. Users (Internal)
-- =========================
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  role ENUM('ADMIN','ANALYST') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- 8. Panelists
-- =========================
CREATE TABLE panelists (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  age INT,
  gender VARCHAR(20),
  country_id BIGINT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_panelists_country
    FOREIGN KEY (country_id) REFERENCES countries(id)
) ENGINE=InnoDB;

-- =========================
-- 9. Questions
-- =========================
CREATE TABLE questions (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  text TEXT NOT NULL,
  question_type ENUM('RATING','TEXT','MCQ') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- 10. Responses
-- =========================
CREATE TABLE responses (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  panelist_id BIGINT NOT NULL,
  question_id BIGINT NOT NULL,
  campaign_id BIGINT NOT NULL,
  response_value TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_responses_panelist
    FOREIGN KEY (panelist_id) REFERENCES panelists(id),

  CONSTRAINT fk_responses_question
    FOREIGN KEY (question_id) REFERENCES questions(id),

  CONSTRAINT fk_responses_campaign
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
) ENGINE=InnoDB;

-- =========================
-- 11. Metrics (Time-Series)
-- =========================
CREATE TABLE metrics (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  campaign_id BIGINT NOT NULL,
  impressions BIGINT DEFAULT 0,
  clicks BIGINT DEFAULT 0,
  conversions BIGINT DEFAULT 0,
  recorded_at DATE NOT NULL,

  CONSTRAINT fk_metrics_campaign
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
) ENGINE=InnoDB;

-- =========================
-- 12. Sentiments
-- =========================
CREATE TABLE sentiments (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  response_id BIGINT NOT NULL,
  sentiment_score DECIMAL(3,2), -- -1.00 to 1.00
  label ENUM('POSITIVE','NEUTRAL','NEGATIVE'),

  CONSTRAINT fk_sentiments_response
    FOREIGN KEY (response_id) REFERENCES responses(id)
) ENGINE=InnoDB;

SET FOREIGN_KEY_CHECKS = 1;
