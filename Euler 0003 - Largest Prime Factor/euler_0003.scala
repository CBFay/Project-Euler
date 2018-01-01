// https://projecteuler.net/problem=3
// created 1.1.2018 by CB Fay

import math.sqrt

object euler_0003 {
    def isprime(n : Long) : Boolean = {
        var i : Long = 2
        var lmt : Long = (sqrt(n) + 1).toLong
        while (i < lmt) {
            if (n % i == 0) {return false} 
            i += 1
        }
        return true
    }
    
    
    def biggestprimefactor(n : Long) : Long = {
        var i : Long = 2
        var lmt : Long = n/2
        while (i < lmt) {
            if (n % i == 0 && isprime(n/i)) {
                return n/i
            }
            i += 1
        }
        return 0
    }
    
    
    def main(args : Array[String]) {
        println(biggestprimefactor(600851475143L))
    }
}
