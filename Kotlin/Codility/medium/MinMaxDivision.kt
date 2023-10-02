fun main() {
    println(solution(3,5, intArrayOf(2,1,5,1,2,2,2)))

}

fun solution(K: Int, M: Int, A: IntArray): Int {
    var start = 0
    var end = A.size * M
    var minMax = Int.MAX_VALUE
    while (start <= end) {
        var mid = (start + end) / 2
        var group = 1
        var sum = 0
        var max = 0
        A.forEach {
            if (sum + it > mid) {
                group += 1
                max = Math.max(max, sum)
                sum = it
            } else {
                sum += it
            }
        }
        max = Math.max(max, sum)

        if (group > K) {
            start = mid + 1
        } else {
            end = mid - 1
            minMax = Math.min(minMax, max)
        }

    }

    return minMax
}