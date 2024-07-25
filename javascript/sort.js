/*
NAME
    sort - sorting and related algorithms

DESCRIPTION
    This module implements a few sorting and related algorithms.

    * insort    insertion sort
    * mgsort    merge sort
    * part      partition
    * part3     Dijkstra's 3-way partitioning
    * qkselect  quick select
    * qksort    quick sort
    * shuffle   shuffle an array in-place

FUNCTIONS

    insort(nums)
        Sort an array in-place into ascending order via insertion sort.

    mgsort(nums)
        Sort an array in-place into ascending order via merge sort.

    part(nums, lo, hi)
        Partition subarray of nums from lo (inclusive) to hi (exclusive).

    part3(nums)
        Partition an array into 3 parts via Dijkstra's 3-way partitioning.

    qkselect(nums, k)
        Return kth smallest element via quick select.

    qksort(nums)
        Sort an array in-place into ascending order via quick sort.

    shuffle(nums)
        Shuffle an array in-place via Knuth's shuffling.
*/

function insort(nums) {
    /*insertion sort*/
    const n = nums.length;
    for (let i = 1; i < n; ++i)
        for (let j = i; j > 0; --j) {
            if (nums[j-1] <= nums[j]) break;
            [nums[j-1], nums[j]] = [nums[j], nums[j-1]];
        }
}


function mgsort(nums) {
    /*merge sort*/

    function sort(nums, aux, lo, hi) {
        if (lo+1 < hi) {
            const mid = Math.floor((lo+hi)/2);
            sort(aux, nums, lo, mid);
            sort(aux, nums, mid, hi);
            let i = lo, j = mid;
            for (let k = lo; k < hi; ++k)
                if (j >= hi || i < mid && aux[i] < aux[j])
                    nums[k] = aux[i++];
                else
                    nums[k] = aux[j++];
        }
    }

    sort(nums, nums.slice(), 0, nums.length);
}


function part(nums, lo, hi) {
    let i = lo+1, j = hi-1;
    while (i <= j) {
        if (nums[i] < nums[lo]) ++i;
        else if (nums[j] > nums[lo]) --j;
        else [nums[i++], nums[j--]] = [nums[j], nums[i]];
    }
    [nums[lo], nums[j]] = [nums[j], nums[lo]];
    return j;
}


function part3(nums) {
    /*Dijkstra's 3-way partition*/
    const n = nums.length;
    let lo = 0, mid = 0, hi = n-1;
    while (mid <= hi)
        if (nums[mid] == 0)
            [nums[lo++], nums[mid++]] = [nums[mid], nums[lo]];
        else if (nums[mid] == 1) ++mid;
        else [nums[hi--], nums[mid]] = [nums[mid], nums[hi]];
}


function qkselect(nums, k) {
    /*quick select*/
    shuffle(nums);
    let lo = 0, hi = nums.length;
    while (lo < hi) {
        const mid = part(nums, lo, hi);
        if (mid < k-1) lo = mid+1;
        else if (mid == k-1) return nums[mid];
        else hi = mid;
    }
}


function qksort(nums, lo=0, hi=-1) {
    /*quick sort by Tony Hoare*/
    if (hi == -1) hi = nums.length;
    if (lo+1 < hi) {
        const mid = part(nums, lo, hi);
        qksort(nums, lo, mid);
        qksort(nums, mid+1, hi);
    }
}


function shuffle(nums) {
    /*Knuth's shuffling*/
    const n = nums.length;
    for (let i = 1; i < n; ++i) {
        const ii = Math.floor(Math.random() * (i+1));
        [nums[ii], nums[i]] = [nums[i], nums[ii]];
    }
}
