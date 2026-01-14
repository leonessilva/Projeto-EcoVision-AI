package com.ecovision.EcoVision.controller;

import com.ecovision.EcoVision.model.Analise;
import com.ecovision.EcoVision.service.AnaliseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/analises")
public class TesteController {

    @Autowired
    private AnaliseService analiseService;

    @PostMapping
    public Analise criarAnalise(@RequestBody Analise analise) {
        return analiseService.processarNovaAnalise(analise);
    }
}