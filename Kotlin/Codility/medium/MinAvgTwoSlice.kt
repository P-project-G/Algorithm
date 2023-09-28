// 수학적인 접근이 필요했던 문제
// 최소 범위의 부분적인 평균은 항상 전체의 평균보다 작을 수 없다
// 그러나 3개의 범위에는 예외가 있기에 평균 값을 구해줘야함
fun main() {
    println(Solution([4,2,2,5,1,5,8]))
    // => 1
}

fun Solution(A: IntArray) {
    val size = A.size
    var minAvg = (A[0] + A[1]) / 2f
    var minStart = Int.MAX_VALUE

    for (i: Int in 2 .. size-1) {
        var res = (A[i] + A[i-1] + A[i-2]) / 3f
        if (minAvg > res) {
            minAvg = res
            minStart = i-2
        }
        res = (A[i] + A[i-1]) / 2f
        if (minAvg > res) {
            minAvg = res
            minStart = i-1
        }
    }

    return minStart
}