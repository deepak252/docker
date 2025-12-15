package com.example.elasticsearch_springboot.repository;

import com.example.elasticsearch_springboot.model.CarModel;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CarRepository extends ElasticsearchRepository<CarModel, String> {
}
