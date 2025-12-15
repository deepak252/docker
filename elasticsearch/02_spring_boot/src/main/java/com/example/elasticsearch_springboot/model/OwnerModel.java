package com.example.elasticsearch_springboot.model;

import lombok.Data;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;

import java.util.List;


@Data
public class OwnerModel {
    @Field(type = FieldType.Text)
    private String name;
    @Field(type = FieldType.Integer)
    private Integer age;
    @Field(type = FieldType.Boolean)
    private Boolean isActive;

}
