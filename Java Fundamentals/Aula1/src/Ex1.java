import java.util.Scanner;
/*
EXEMPLO 1 - SOMAE DOIS NÚMEROS

Desenvolva um programa que faça a soma de dois números e mostre o total.

 */

public class Ex1 {
    public static void main(String[] args){
        //Instanciando e criando um objeto do tipo scanner
        Scanner ler = new Scanner(System.in);

        //DECLARANDO AS VARIÁVEIS
        int num1;
        int num2;
        int resultado;

        //ENTRADA DE DADOS
        System.out.println("Digite o primeiro número: ");
        num1 = ler.nextInt();

        System.out.println("Digite o segundo número: ");
        num2 = ler.nextInt();

        resultado = num1 + num2;

        System.out.println("Resultado: " + resultado);
    }
}
