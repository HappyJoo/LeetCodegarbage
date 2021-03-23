// Bubble sort
// time pass, but should be correct
// Reference: https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
// TIME： O(N2)
// SPACE: O(1)

func sortArray(nums []int) []int {

	for i := 0; i < len(nums)-1; i++ {
		t := true
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > nums[j] {
				nums[i], nums[j] = nums[j], nums[i]
				t = false
			}
		}
		if t == true {
			break
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