"""
NAME 
    sort - sorting and related algorithms 

DESCRIPTION 
    This module implements a few sorting and related algorithms. 

    * shuffle  - shuffle an array in-place
    * insort   - insertion sort 
    * qksort   - quick sort
    * mgsort   - merge sort 
    * qkselect - quick select
    * part3    - Dijkstra's 3-way partitioning

FUNCTIONS
    shuffle(nums)
        Shuffle an array in-place via Knuth's shuffling.

    insort(nums)
        Sort an array in-place into ascending order via insertion sort.

    qksort(nums)
        Sort an array in-place into ascending order via quick sort.

    mgsort(nums)
        Sort an array in-place into ascending order via merge sort.

    qkselect(nums, k)
        Return kth smallest element via quick select. 

    part3(nums)
        Partition an array into 3 parts via Dijkstra's 3-way partitioning.
"""


def shuffle(nums: List[int]) -> None: 
    """Shuffle an array in-place via Knuth's shuffling."""
    for i in range(1, len(nums)): 
        ii = randint(0, i)
        if ii != i: nums[ii], nums[i] = nums[i], nums[ii]


def insort(nums: List[int]) -> None:
    """Sort an array in-place into ascending order via insertion sort."""
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j-1] <= nums[j]: break
            nums[j-1], nums[j] = nums[j], nums[j-1]


def qksort(nums: List[int]) -> None:
    """Sort an array in-place into ascending order via quick sort."""
    shuffle(nums)                
        
    def sort(lo, hi): 
        """Sort nums[lo:hi] via quick sort."""
        if lo + 1 == hi: return 
        i, j = lo+1, hi-1
        while i <= j: 
            if nums[i] < nums[lo]: i += 1
            elif nums[j] > nums[lo]: j -= 1
            else: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        sort(lo, j)
        sort(j+1, hi)
        
    sort(0, len(nums))


def mgsort(nums: List[int]) -> None:
    """Sort an array in-place into ascending order via merge sort."""
    
    def sort(nums, aux, lo, hi): 
        """Sort nums[lo:hi] via merge sort."""
        if lo+1 >= hi: return 
        mid = lo + hi >> 1
        sort(aux, nums, lo, mid)
        sort(aux, nums, mid, hi)
        i, j = lo, mid
        for k in range(lo, hi): 
            if j >= hi or i < mid and aux[i] < aux[j]: 
                nums[k] = aux[i]
                i += 1
            else: 
                nums[k] = aux[j]
                j += 1
    
    sort(nums, nums.copy(), 0, len(nums))


def qkselect(nums: List[int], k: int) -> int:
    """Return kth smallest element via quick select."""
    shuffle(nums)

    def part(lo, hi):
        """Return partition of nums[lo:hi]."""
        i, j = lo+1, hi-1
        while i <= j: 
            if nums[i] < nums[lo]: i += 1
            elif nums[lo] < nums[j]: j -= 1
            else: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j 

    lo, hi = 0, len(nums)
    while lo < hi: 
        mid = part(nums, lo, hi)
        if mid < k-1: lo = mid + 1
        elif mid == k-1: return nums[mid]
        else: hi = mid


def part3(nums: List[int]) ->None: 
    """Partition an array into 3 parts via Dijkstra's 3-way partitioning."""
    lo, mid, hi = 0, 0, len(nums)-1
    while mid <= hi: 
        if nums[mid] == 0: 
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1: mid += 1
        else: 
            nums[hi], nums[mid] = nums[mid], nums[hi]
            hi -= 1