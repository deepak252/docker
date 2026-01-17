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
-- 2. Media Channels
-- =========================
CREATE TABLE media_channels (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  type VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- 3. Companies
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
-- 4. Products
-- =========================
CREATE TABLE products (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  company_id BIGINT NOT NULL,
  media_channel_id BIGINT NOT NULL,
  country_id BIGINT NOT NULL,

  title VARCHAR(255) NOT NULL,
  description VARCHAR(10000),
  category VARCHAR(100),

  start_date DATE,
  end_date DATE,
  budget DECIMAL(12,2),

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_products_company
    FOREIGN KEY (company_id) REFERENCES companies(id),

  CONSTRAINT fk_products_channel
    FOREIGN KEY (media_channel_id) REFERENCES media_channels(id),

  CONSTRAINT fk_products_country
    FOREIGN KEY (country_id) REFERENCES countries(id)
) ENGINE=InnoDB;

-- =========================
-- 5. Product Media (Images / Videos / PDFs) (one-many relationship)
-- =========================
CREATE TABLE product_media (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  product_id BIGINT NOT NULL,

  media_type ENUM('IMAGE','VIDEO','PDF') NOT NULL,
  media_url TEXT NOT NULL,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_product_media_product
    FOREIGN KEY (product_id) REFERENCES products(id)
) ENGINE=InnoDB;

SET FOREIGN_KEY_CHECKS = 1;
