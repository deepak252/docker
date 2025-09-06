package com.example.api.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

@RestController
public class ApiController {
    
    @GetMapping("/")
    public String hello() {
        return "Hello from Spring Boot!";
    }
    
    @GetMapping("/heavy")
    public Map<String, Integer> heavy() {
        int total = 0;
        for (int i = 0; i < 100000; i++) {
            total += i;
        }
        return Map.of("total", total);
    }
}