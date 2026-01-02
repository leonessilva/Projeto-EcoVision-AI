package com.ecovision.EcoVision.controller;

import com.ecovision.EcoVision.repository.AnaliseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller // Note que aqui NÃO é RestController, é Controller de telas
public class WebController {

    @Autowired
    private AnaliseRepository repository;

    @GetMapping("/") // Quando acessar http://localhost:8081, cai aqui
    public String paginaInicial(Model model) {
        // Pega tudo do banco e manda para o HTML
        model.addAttribute("listaDeAnalises", repository.findAll());
        return "dashboard"; // Nome do arquivo HTML que vamos criar
    }
}