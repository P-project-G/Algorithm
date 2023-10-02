
import java.util.Stack
fun main() {
    println(solution4("(()(())())"))
    println(solution4("(()"))
}

fun solution4(S: String): Int {

    var stack: Stack<Char> = Stack()

    S.forEach {
        if (it.equals('(')) {
            stack.push('(')
        } else {
            if (stack.size > 0) {
                stack.pop()
            } else {
                return 0
            }
        }
    }

    if (stack.size > 0) {
        return 0
    }

    return 1
}