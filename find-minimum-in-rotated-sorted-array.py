            mid = (l + h) // 2

            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid

        return nums[l]
        while l < h:
