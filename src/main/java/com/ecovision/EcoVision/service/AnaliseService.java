package com.ecovision.EcoVision.service;

import com.ecovision.EcoVision.GeradorRelatorio;
import com.ecovision.EcoVision.model.Analise;
import com.ecovision.EcoVision.repository.AnaliseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;

@Service
public class AnaliseService {

    @Autowired
    private AnaliseRepository repository;

    public Analise processarNovaAnalise(Analise novaAnalise) {
        novaAnalise.setDataHora(LocalDateTime.now());
        
        // 1. Salva no Banco
        Analise analiseSalva = repository.save(novaAnalise);
        
        // 2. Salva no CSV (Usando o seu gerador profissional)
        GeradorRelatorio.salvarNoArquivo(analiseSalva);
        
        return analiseSalva;
    }
}