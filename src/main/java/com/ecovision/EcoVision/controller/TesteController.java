package com.ecovision.EcoVision.controller;

import com.ecovision.EcoVision.model.Analise;
import com.ecovision.EcoVision.repository.AnaliseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*; // Importa tudo necessário para web

import java.time.LocalDateTime;

@RestController
@RequestMapping("/analises") // Mudamos o nome para algo mais profissional
public class TesteController {

    @Autowired
    private AnaliseRepository repository;

    // AGORA É UM POST: Recebe dados de fora (JSON)
    @PostMapping
    public Analise receberNovaAnalise(@RequestBody Analise novaAnalise) {
        
        // Define a hora exata que chegou no sistema
        novaAnalise.setDataHora(LocalDateTime.now());
        
        // Salva no banco o que veio no JSON
        return repository.save(novaAnalise);
    }
}