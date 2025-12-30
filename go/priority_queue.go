type PriorityQueue []int

func (pq PriorityQueue) Len() int {
    return len(pq)
}

func (pq PriorityQueue) Less(i int, j int) bool {
    return pq[i] < pq[j]
}

func (pq PriorityQueue) Swap(i int, j int) {
    pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(elem any) {
    val := elem.(int)
    *pq = append(*pq, val)
}

func (pq *PriorityQueue) Pop() any {
    val := (*pq)[pq.Len() - 1]
    *pq = (*pq)[0 : pq.Len() - 1]
    return val
}
