package PasoPorValor;

public class pasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); // Solo le enviamos una copia
        System.out.println("valorX = " + valorX);
    }
    public static void cambioValor(int arg1){ //parametos por valor
        System.out.println("arg1 = " + arg1);
        arg1 = 15;
    }
}