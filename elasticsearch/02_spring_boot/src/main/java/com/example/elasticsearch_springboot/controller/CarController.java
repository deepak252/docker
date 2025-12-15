package com.example.elasticsearch_springboot.controller;

import com.example.elasticsearch_springboot.model.CarModel;
import com.example.elasticsearch_springboot.repository.CarRepository;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/car")
public class CarController {
    private final CarRepository carRepository;

    @Autowired
    public CarController(CarRepository carRepository) {
        this.carRepository = carRepository;
    }

    @PostMapping
    public void save(@RequestBody CarModel car){
        carRepository.save(car);
    }

    @GetMapping("/{id}")
    public CarModel findById(@PathVariable String id){
        return carRepository.findById(id).orElse(null);
    }

    @GetMapping
    public Iterable<CarModel> findAll(){
        return carRepository.findAll();
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable String id){
        carRepository.deleteById(id);
    }

    @PutMapping
    public void update(@RequestBody CarModel car){
        carRepository.save(car);
    }
}
