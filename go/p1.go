// if we list all the natural numbers below 10 that
// are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
// these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.


// `for` is Go's only looping construct. Here are
// three basic types of `for` loops.

package main

import "fmt"

func sum_of_multiples_under(number int) int {
    var sum int = 0

    i := 1
    for i < number {

        if i%3 == 0 {
            sum = sum + i
        } else if i%5 == 0 {
            sum = sum + i
        }

        i = i + 1
    }

    return sum
}

func main() {
    res := sum_of_multiples_under(1000)
    fmt.Println(res)
}
