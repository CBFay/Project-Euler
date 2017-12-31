// https://projecteuler.net/problem=1
// created 12.30.2017 by CB Fay

object solution {
    def main(args : Array[String]) {
        var multiples : Set[Int] = Set()
        
        for (i <- 3 until 1000 if i % 3 == 0) {
            multiples += i
        }
        
        for (i <- 5 until 1000 if i % 5 == 0) {
            multiples += i
        }
        
        println(multiples.sum)
    }
}
