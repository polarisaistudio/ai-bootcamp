# parameter_lab.py
import openai
import time
from typing import List

class ParameterLab:
    """参数实验室"""

    def __init__(self):
        self.client = openai.OpenAI()
        self.results = []

    def experiment_temperature(self,
                              prompt: str,
                              temperatures: List[float] = [0, 0.5, 1.0, 1.5],
                              n_samples: int = 3):
        """Temperature实验"""

        print(f"🧪 Temperature实验")
        print(f"Prompt: {prompt}")
        print("=" * 60)

        for temp in temperatures:
            print(f"\n🌡️ Temperature = {temp}")
            print("-" * 40)

            samples = []
            for i in range(n_samples):
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temp,
                    max_tokens=30
                )

                text = response.choices[0].message.content
                samples.append(text)
                print(f"  样本{i+1}: {text}")

            # 计算多样性
            diversity = self._calculate_diversity(samples)
            print(f"  📊 多样性得分: {diversity:.2f}")

    def _calculate_diversity(self, texts: List[str]) -> float:
        """计算文本多样性"""
        if len(texts) < 2:
            return 0.0

        all_words = []
        for text in texts:
            all_words.extend(text.split())

        unique_words = set(all_words)
        diversity = len(unique_words) / len(all_words) if all_words else 0

        return diversity

# 使用示例
if __name__ == "__main__":
    lab = ParameterLab()

    # 测试创意写作
    lab.experiment_temperature("用一句话描述夕阳")

    # 测试事实查询
    lab.experiment_temperature("中国的首都是", temperatures=[0, 0.5, 1.0])
