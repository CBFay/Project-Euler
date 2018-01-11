// https://projecteuler.net/problem=9
// created 1.11.2018 by CB Fay

import math.{sqrt, pow}

object euler_0009 {
    def main(args : Array[String]) {
        var a : Double = 1
        var b : Double = 1
        var c : Double = 1
        while (a < 500) {
            a += 1
            b = a + 1
            while (b < 500) {
                b += 1
                c = sqrt(pow(a, 2) + pow(b, 2))
                if (a + b + c == 1000) {
                    println(a, b, c)
                    println((a * b * c).toLong)
                }
            }
        }
    }
}
