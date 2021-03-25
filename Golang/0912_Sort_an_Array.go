// https://leetcode-cn.com/problems/sort-an-array/
// Bubble sort
// time pass, but should be correct
// time pass is because Bubble sort require two more steps then Insertion and Selection
// Reference: https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
// TIME： O(N2)
// SPACE: O(1)

func sortArray(nums []int) []int {
	n := len(nums)
	if n == 0 {
		return nums
	}

	for i := 0; i < n; i++ {
		flag := true
		for j := 0; j < n-i-1; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
				flag = false
			}
		}
		if flag {
			return nums
		}
	}
	return nums
}

// Insertion sort
// TIME： O(N2)
// SPACE: O(1)
func sortArray(nums []int) []int {

	for i := 1; i < len(nums); i++ {
		temp := nums[i]
		j := i - 1
		for ; j >= 0; j-- {
			if nums[j] > temp {
				nums[j+1] = nums[j]
			} else {
				break
			}
		}
		nums[j+1] = temp
	}
	return nums
}

// Selection sort
// TIME： O(N2)
// SPACE: O(1)
func sortArray(nums []int) []int {
	for i := 0; i < len(nums)-1; i++ {
		tempIndex := i
		for j := i + 1; j < len(nums); j++ {
			if nums[j] < nums[tempIndex] {
				tempIndex = j // always store the smallest number index
			}
		}
		nums[i], nums[tempIndex] = nums[tempIndex], nums[i]
	}
	return nums
}

// Merge sort
// TIME： O(Nlog(N))
// SPACE: O(N)
func sortArray(nums []int) []int {
	n := len(nums)
	if n < 2 {
		return nums
	}
	i := n / 2

	left := sortArray(nums[:i])
	right := sortArray(nums[i:])
	return merge(left, right)
}

func merge(l, r []int) []int {
	i, j := 0, 0
	m, n := len(l), len(r)
	var res []int
	for i < m && j < n {
		if l[i] < r[j] {
			res = append(res, l[i])
			i++
		} else {
			res = append(res, r[j])
			j++
		}
	}
	res = append(res, l[i:]...)
	res = append(res, r[j:]...)
	return res
}