import click
from datetime import date
from src.services.card_calculator import calculate_best_card, get_current_billing_cycle
from src.services.data_persistence import save_cards, load_cards
from src.models.credit_card import CreditCard


@click.group()
def cli():
    """信用卡管理系统的命令行界面"""
    pass


@cli.command()
@click.option('--name', prompt='卡片名称', help='信用卡的名称')
@click.option('--bill-day', prompt='账单日', type=int, help='每月账单生成的日期')
@click.option('--repay-day', prompt='还款日', type=int, help='每月还款的截止日期')
@click.option('--credit-limit', prompt='信用额度', type=float, help='信用卡的额度')
def add_card(name, bill_day, repay_day, credit_limit):
    """添加新的信用卡到系统中"""
    card = CreditCard(name, bill_day, repay_day, credit_limit)
    if not card.is_valid():
        click.echo("无效的卡片信息。请检查您的输入。")
        return

    cards = load_cards()
    cards.append(card)
    save_cards(cards)
    click.echo(f"卡片 '{name}' 已成功添加。")


@cli.command()
def best_card():
    """计算并显示今天最适合使用的信用卡"""
    cards = load_cards()
    if not cards:
        click.echo("未找到任何卡片。请先添加一张卡片。")
        return

    best = calculate_best_card(cards)
    if best:
        click.echo(f"今天最适合使用的卡片是：{best.name}")
    else:
        click.echo("未找到合适的卡片。")


@cli.command()
@click.option('--date', 'target_date', default=str(date.today()), help='指定日期 (YYYY-MM-DD 格式)')
def show_cycles(target_date):
    """显示所有信用卡的当前或最近账单周期信息"""
    cards = load_cards()
    if not cards:
        click.echo("未找到任何卡片。请先添加一张卡片。")
        return

    try:
        target_date = date.fromisoformat(target_date)
    except ValueError:
        click.echo("无效的日期格式。请使用 YYYY-MM-DD 格式。")
        return

    click.echo(f"日期：{target_date}")
    click.echo("-" * 50)

    for card in cards:
        cycle_start, cycle_end, repay_date = get_current_billing_cycle(card, target_date)

        if cycle_start <= target_date <= cycle_end:
            cycle_status = "当前"
        else:
            cycle_status = "最近"

        click.echo(f"卡片：{card.name}")
        click.echo(f"{cycle_status}账单周期：{cycle_start} 至 {cycle_end}")
        click.echo(f"还款日：{repay_date}")
        click.echo(f"可用额度：{card.available_credit()}")
        click.echo("-" * 50)


if __name__ == '__main__':
    cli()