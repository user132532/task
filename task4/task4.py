import sys

def calculate_min_moves(nums):
    # Сортируем массив для нахождения медианы
    nums_sorted = sorted(nums)
    median = nums_sorted[len(nums) // 2]  # Медиана — средний элемент отсортированного массива
    
    # Вычисляем сумму абсолютных разностей между элементами и медианой
    total_moves = sum(abs(num - median) for num in nums)
    
    return total_moves