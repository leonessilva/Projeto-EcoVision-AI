package com.ecovision.EcoVision;

import com.ecovision.EcoVision.model.Analise;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class GeradorRelatorio {

    private static final String NOME_ARQUIVO = "dados_biologicos.csv";

    public static void salvarNoArquivo(Analise analise) {
        try {
            // Verifica se o arquivo já existe para decidir se cria o cabeçalho
            File arquivo = new File(NOME_ARQUIVO);
            boolean arquivoNovo = !arquivo.exists();

            // O "true" aqui significa: "Não apague o que já tem, escreva no final (append)"
            FileWriter fw = new FileWriter(NOME_ARQUIVO, true);
            PrintWriter escritor = new PrintWriter(fw);

            // Se for arquivo novo, escreve os títulos das colunas (Cabeçalho)
            if (arquivoNovo) {
                escritor.println("Data,Hora,Especie,Quantidade,ConfiancaIA,Local");
            }

            // Formata a data e hora bonitinho
            LocalDateTime agora = LocalDateTime.now();
            String data = agora.format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));
            String hora = agora.format(DateTimeFormatter.ofPattern("HH:mm:ss"));

            // Escreve a linha de dados (separados por vírgula)
            escritor.printf("%s,%s,%s,%d,%.1f,%s%n",
                data,
                hora,
                analise.getEspecie(),
                analise.getQuantidade(),
                analise.getConfiancaIA(),
                analise.getLocalColeta()
            );

            escritor.close(); // Fecha o arquivo para salvar
            System.out.println("💾 Dados salvos no Excel (CSV) com sucesso!");

        } catch (Exception e) {
            System.out.println("❌ Erro ao salvar no arquivo: " + e.getMessage());
        }
    }
}