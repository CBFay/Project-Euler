// https://projecteuler.net/problem=2
// created 12.30.2017 by CB Fay

object euler_0002 {
    def main(args : Array[String]) {
        var s = 0 // sum
        var a = 1
        var b = 2
        while (b < 4000000) {
            if (b % 2 == 0) {s += b}
            b = b+a
            a = b-a
        }
        println(s)
    }
}
