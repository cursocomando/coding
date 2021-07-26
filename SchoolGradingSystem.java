/*package App;*/

import java.util.*;
public class SchoolGradingSystem {
    static final String[] nombres
            = {"armando", "nicolas", "daniel", "maria", "marcela", "alexandra"};
    static final String[] materias = {"idiomas", "historia", "literatura"};
    static final String[] generos = {"m", "f"};

    static String[] nombresProblema;
    static String[] materiasProblema;
    static String[] generosProblema;
    static double[] calificacionesProblema;
    static int n; //cantidad de estudiantes

    public void readData(){
        Scanner scanner = new Scanner(System.in);
        this.n = scanner.nextInt();
        this.nombresProblema = new String[n];
        this.materiasProblema = new String[n];
        this.generosProblema = new String[n];
        this.calificacionesProblema = new double[n];


        for(int i=0; i<n; i++){ //i++ = i = i+1 = i += 1
            String nombre = nombres[(int)scanner.nextDouble()-1];
            nombresProblema[i] = nombre;
            //System.out.print(nombresProblema[i] + " ");
            String genero = generos[(int)scanner.nextDouble()];
            generosProblema[i] = genero;
            //System.out.print(generosProblema[i] + " ");
            String materia = materias[(int)scanner.nextDouble()-1];
            materiasProblema[i] = materia;
            //System.out.print(materiasProblema[i] + " ");
            double calificacion = scanner.nextDouble();
            calificacionesProblema[i] = calificacion;
            //System.out.println(calificacionesProblema[i]);
        }
        scanner.close();
    }
    public double question1(){
        double suma = 0;
        for(int i = 0; i<this.n; i++){
            suma += this.calificacionesProblema[i];
        }
        double promedio = suma/this.n;

        suma = 0;
        for(int i =0; i<this.n; i++){
            suma += Math.pow(this.calificacionesProblema[i] - promedio, 2);
        }
        double varianza = suma/(this.n);
        varianza = Math.round(varianza*100.0)/100.0;
        return varianza;
    }

    public double question2(){
        double contador = 0;
        for(int i = 0; i<this.n; i++){
            if(this.calificacionesProblema[i] <= 9.0 && this.calificacionesProblema[i] > 8.0){
                contador++;
            }
        }
        contador = Math.round((contador/this.n)*100.0)/100.0;
        return contador;
    }

    public String question3(){
        double promedioM = 0;
        double contadorM = 0;
        double promedioF = 0;
        double contadorF = 0;
        for(int i = 0; i<this.calificacionesProblema.length; i++){
            if(this.generosProblema[i].equals("m")){
                promedioM += this.calificacionesProblema[i];
                contadorM ++;
            }
            else{
                promedioF += this.calificacionesProblema[i];
                contadorF++;
            }
        }
        promedioM = promedioM/contadorM;
        promedioF = promedioF/contadorF;
        if(promedioM>=promedioF) return "m";
        else return "f";

    }
    public String question4(){
        double mayor = -1.0;
        String nombreMayor = "";
        for(int i = 0; i<this.calificacionesProblema.length; i++){
            if(this.materiasProblema[i].equals("idiomas")){
                if(this.calificacionesProblema[i]>mayor){
                    mayor = this.calificacionesProblema[i];
                    nombreMayor = this.nombresProblema[i];
                }
                else if(this.calificacionesProblema[i] == mayor){
                    for(int j = 0; i<nombres.length; j++){
                        if(this.nombresProblema[i].equals(nombres[j])){
                            mayor = this.calificacionesProblema[i];
                            nombreMayor = this.nombresProblema[i];
                            break;
                        }
                        if(nombreMayor.equals(nombres[j])){
                            break;
                        }

                    }


                }
            }
        }
        return nombreMayor;
    }
}
