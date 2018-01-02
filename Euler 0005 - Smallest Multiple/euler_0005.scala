// https://projecteuler.net/problem=5
// created 1.1.2018 by CB Fay

object euler_0005 {
    def main(args : Array[String]) {
        var n = 2520
        while (true) {
            n += 2520
            var div = 1
            while (div <= 20) {
                div += 1
                if (n % div != 0) {div = 21}
                if (div == 20) {proof(n); return}
            }
        }
    }
    
    def proof(n : Int) {
        for (i <- 1 until 20) {
            println(n + " / " + i + " = " + n/i)
        }
    }
}
