
// https://projecteuler.net/problem=10
// created 1.12.2018 by CB Fay

object euler_0010 {
    def main(args : Array[String]) {
        var prime = Array.fill[Boolean](2000001)(true)
        var sum : Long = 0
        var p : Long = 2
        while (p < 2000000) {
            var composite = false
            if (prime(p.toInt) == false) {
                composite = true
            }
            if (composite == false) {
                sum += p
                var multi : Long = p
                while (multi < 2000000 / p + 1) {
                    prime((p*multi).toInt) = false;
                    multi += 1
                }
            }
            p += 1
        }
        println(sum)
    }
}
