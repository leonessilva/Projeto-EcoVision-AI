package com.ecovision.EcoVision.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity 
public class Analise {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime dataHora;
    private String localColeta;
    private String especie;
    private Double confiancaIA;
    private Integer quantidade;

    // Construtor vazio (Necessário para o Hibernate funcionar)
    public Analise() {
    }

    // Construtor completo
    public Analise(Long id, LocalDateTime dataHora, String localColeta, String especie, Double confiancaIA, Integer quantidade) {
        this.id = id;
        this.dataHora = dataHora;
        this.localColeta = localColeta;
        this.especie = especie;
        this.confiancaIA = confiancaIA;
        this.quantidade = quantidade;
    }

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public LocalDateTime getDataHora() { return dataHora; }
    public void setDataHora(LocalDateTime dataHora) { this.dataHora = dataHora; }

    public String getLocalColeta() { return localColeta; }
    public void setLocalColeta(String localColeta) { this.localColeta = localColeta; }

    public String getEspecie() { return especie; }
    public void setEspecie(String especie) { this.especie = especie; }

    public Double getConfiancaIA() { return confiancaIA; }
    public void setConfiancaIA(Double confiancaIA) { this.confiancaIA = confiancaIA; }

    public Integer getQuantidade() { return quantidade; }
    public void setQuantidade(Integer quantidade) { this.quantidade = quantidade; }
}