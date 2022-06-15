#include <vector>
#include <iostream>
double max(double a, double b) {
    if (a > b) return a;
    return b;
}

double findMaxAverage(std::vector<int>& nums, int k) {
    double max_sum;
    for (int i = 0; i < k; i +=1) {
      max_sum += (double)nums[i];
    }
    double current_sum = max_sum;
    int left = 1;
    int right = k;
    while (right < nums.size()) {
      current_sum = (double)(current_sum - nums[left-1] + nums[right]);
      max_sum = max(max_sum, current_sum);
      right +=1;
      left +=1;
    }
    return (double)(max_sum / k);
}


int main() {
  std::vector<int> nums = {1,12,-5,-6,50,3};
  int k = 4;
  double res = findMaxAverage(nums, k);
  std::cout << res << "\n";
}
