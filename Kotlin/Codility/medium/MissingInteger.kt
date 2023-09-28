fun Solution(A: IntArray) {
    var dict: SortedMap<Int, Int> = sortedMapOf<Int, Int>()

    A.forEach {
        if (it > 0) {
            dict.put(it, dict.get(it)?.plus(1) ?: 1)
        }
    }

    var prev = 1
    if (dict.size == 0) {
        return 1
    } else {
        dict.forEach {
            if (prev != it.key) {
                return prev
            }
            prev += 1
        }
    }

    return prev
}
fun main() {
    println(Solution(intArrayOf(1,2,3,4,5,2,1,1,7)))
}

