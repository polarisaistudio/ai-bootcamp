# token_economics.py
import tiktoken
import matplotlib.pyplot as plt

class TokenEconomicsDemo:
    def __init__(self):
        self.encoder = tiktoken.get_encoding("cl100k_base")

    def compare_languages(self):
        """对比不同语言的Token效率"""

        test_cases = {
            'English': "Artificial Intelligence is transforming the world",
            '中文': "人工智能正在改变世界",
            '日本語': "人工知能は世界を変えています",
            'Code': "def hello(): return 'world'",
            'Mixed': "AI(人工智能) is 改变ing the world"
        }

        print("🌍 多语言Token效率对比")
        print("-" * 50)

        results = []
        for lang, text in test_cases.items():
            tokens = self.encoder.encode(text)
            char_count = len(text)
            token_count = len(tokens)
            efficiency = char_count / token_count

            print(f"\n{lang}:")
            print(f"  文本: {text}")
            print(f"  字符数: {char_count}")
            print(f"  Token数: {token_count}")
            print(f"  效率比: {efficiency:.2f}")

            results.append({
                'Language': lang,
                'Tokens': token_count,
                'Efficiency': efficiency
            })

        return results

# 成本计算实战
def calculate_cost(text, model='gpt-3.5-turbo', calls_per_day=1000):
    """实时计算API成本"""

    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = len(encoder.encode(text))

    # 价格表（2025年最新）
    pricing = {
        'gpt-5': 0.05,  # $0.05/1K tokens输入
        'gpt-4.5-turbo': 0.015,
        'gpt-4o': 0.0075,
        'gpt-4o-mini': 0.0004,
        'gpt-3.5-turbo': 0.0005,
        'claude-sonnet-4.5': 0.003,
        'gemini-2.0-pro': 0.002
    }

    cost_per_call = (tokens / 1000) * pricing[model]
    daily_cost = cost_per_call * calls_per_day
    monthly_cost = daily_cost * 30

    print(f"📝 Token数: {tokens}")
    print(f"💵 单次成本: ${cost_per_call:.6f}")
    print(f"📅 日成本({calls_per_day}次): ${daily_cost:.2f}")
    print(f"📆 月成本: ${monthly_cost:.2f}")
    print(f"🎯 年成本: ${monthly_cost*12:.2f}")

    return monthly_cost

def compare_all_models(text, calls_per_day=1000):
    """比较所有模型的成本"""

    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = len(encoder.encode(text))

    # 价格表（2025年最新）
    pricing = {
        'gpt-5': 0.05,  # $0.05/1K tokens输入
        'gpt-4.5-turbo': 0.015,
        'gpt-4o': 0.0075,
        'gpt-4o-mini': 0.0004,
        'gpt-3.5-turbo': 0.0005,
        'claude-sonnet-4.5': 0.003,
        'gemini-2.0-pro': 0.002
    }

    print(f"📝 Token数: {tokens}")
    print(f"📞 每日调用次数: {calls_per_day}")
    print("\n" + "="*70)

    results = []
    for model, price in pricing.items():
        cost_per_call = (tokens / 1000) * price
        daily_cost = cost_per_call * calls_per_day
        monthly_cost = daily_cost * 30
        yearly_cost = monthly_cost * 12

        results.append({
            'model': model,
            'price_per_1k': price,
            'cost_per_call': cost_per_call,
            'daily_cost': daily_cost,
            'monthly_cost': monthly_cost,
            'yearly_cost': yearly_cost
        })

        print(f"\n{model}:")
        print(f"  价格: ${price}/1K tokens")
        print(f"  单次成本: ${cost_per_call:.6f}")
        print(f"  日成本: ${daily_cost:.2f}")
        print(f"  月成本: ${monthly_cost:.2f}")
        print(f"  年成本: ${yearly_cost:.2f}")

    print("\n" + "="*70)
    return results

def plot_cost_comparison(results):
    """Plot cost comparison charts"""

    models = [r['model'] for r in results]
    monthly_costs = [r['monthly_cost'] for r in results]
    yearly_costs = [r['yearly_cost'] for r in results]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Monthly cost comparison
    bars1 = ax1.bar(range(len(models)), monthly_costs, color='skyblue', edgecolor='navy')
    ax1.set_xlabel('Model', fontsize=12)
    ax1.set_ylabel('Monthly Cost ($)', fontsize=12)
    ax1.set_title('Monthly Cost Comparison (1000 calls/day)', fontsize=14, fontweight='bold')
    ax1.set_xticks(range(len(models)))
    ax1.set_xticklabels(models, rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.2f}',
                ha='center', va='bottom', fontsize=9)

    # Yearly cost comparison
    bars2 = ax2.bar(range(len(models)), yearly_costs, color='lightcoral', edgecolor='darkred')
    ax2.set_xlabel('Model', fontsize=12)
    ax2.set_ylabel('Yearly Cost ($)', fontsize=12)
    ax2.set_title('Yearly Cost Comparison (1000 calls/day)', fontsize=14, fontweight='bold')
    ax2.set_xticks(range(len(models)))
    ax2.set_xticklabels(models, rotation=45, ha='right')
    ax2.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.2f}',
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('model_cost_comparison.png', dpi=300, bbox_inches='tight')
    print("\n📊 Chart saved as 'model_cost_comparison.png'")
    plt.show()

if __name__ == "__main__":
    # Run the token economics demo
    demo = TokenEconomicsDemo()

    print("\n" + "="*50)
    results = demo.compare_languages()

    print("\n" + "="*50)
    print("\n💰 成本计算示例")
    print("-" * 50)

    # Example cost calculation
    example_text = "Artificial Intelligence is transforming the world through machine learning and deep learning."
    print(f"\n示例文本: {example_text}\n")

    # 对比所有模型
    print("\n" + "="*70)
    print("📊 所有模型成本对比")
    print("="*70)
    model_results = compare_all_models(example_text, calls_per_day=1000)

    # 绘制对比图表
    plot_cost_comparison(model_results)
