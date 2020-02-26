/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package compu;

import Mouse.Mouse;
import Procesador.Procesador;
import Teclado.Teclado;

/**
 *
 * @author rodau
 */
public class Compu {
    
    private String marca;
    private String modelo;
    Procesador porc1 = new Procesador();
    Teclado tec1 = new Teclado();
    Mouse mou1 = new Mouse();
    
    public void encender (){
        System.out.println("Encendiendo");
        porc1.encender();
        
    }
    
    public void funcionar (){
        mou1.seleccionar();
        tec1.escribir();
    }
    public void apagar(){
        System.out.println("Apagar");
        porc1.apagar();
    }
    
    
    
    
    public static void main(String[] args) {
        Compu com1 = new Compu();
        com1.encender();
        com1.funcionar();
        com1.apagar();
        
        
        
    }
    
}
