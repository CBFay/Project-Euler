// https://projecteuler.net/problem=2
// created 12.30.2017 by CB Fay

object Solution {
    def main(args : Array[String]) {
        var a = 1
        var b = 2
        var s = 0 // sum
        while (b < 4000000) {
            if (b % 2 == 0) {s += b}
            b += a
            a = b-a
        }
        println(sum)
    }
}
