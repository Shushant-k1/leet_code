class Solution {
public:
    string countAndSay(int n) {
        string ans = "1";
        for (int j = 1; j < n; j++) {
            string tem = "";
            int cnt = 1;
            for (int i = 1; i < ans.size(); i++) {
                if (ans[i] != ans[i - 1]) {
                    tem += to_string(cnt);
                    tem += ans[i - 1];
                    cnt = 1;
                } else {
                    cnt++;
                }
            }
            tem += to_string(cnt);
            tem += ans.back();
            ans = tem;
        }
        return ans;
    }
};
