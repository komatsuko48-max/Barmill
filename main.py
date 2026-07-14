import flet as ft
import data
import traceback

def main(page: ft.Page):
    page.title = "Barmill Offer"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    try:
        # data.offers ကို စစ်မယ်
        if not data.offers:
            page.add(
                ft.Container(
                    content=ft.Text(
                        "⚠️ ဒေတာမရှိပါ။\n\ndata.json ဖိုင် မပါဝင်နိုင်ပါ။",
                        size=18,
                        color=ft.colors.RED_700,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    padding=30,
                    bgcolor=ft.colors.RED_50,
                    border_radius=10,
                )
            )
            return

        # ဇယားခေါင်းစဉ်များ
        columns = [
            ft.DataColumn(ft.Text("No.", weight="bold")),
            ft.DataColumn(ft.Text("Item", weight="bold")),
            ft.DataColumn(ft.Text("Code", weight="bold")),
            ft.DataColumn(ft.Text("Drawing", weight="bold")),
            ft.DataColumn(ft.Text("Price (USD)", weight="bold")),
        ]

        rows = []
        for idx, item in enumerate(data.offers[:200]):
            try:
                rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(item.get("No.", "")))),
                            ft.DataCell(ft.Text(str(item.get("Item", "")))),
                            ft.DataCell(ft.Text(str(item.get("Code", "")))),
                            ft.DataCell(ft.Text(str(item.get("96/3805 Drawing no.", "")), max_lines=2)),
                            ft.DataCell(ft.Text(str(item.get("Unit Price (USD)", "")))),
                        ]
                    )
                )
            except Exception as row_error:
                print(f"Row {idx} error: {row_error}")

        table = ft.DataTable(
            columns=columns,
            rows=rows,
            border=ft.border.all(1, ft.colors.GREY_400),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_300),
            horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_300),
            heading_row_color=ft.colors.BLUE_100,
            heading_row_height=40,
            data_row_max_height=60,
        )

        page.add(
            ft.Text("🛠️ Barmill Offer - Spare Parts", size=28, weight="bold"),
            ft.Divider(height=10, thickness=2),
            ft.Container(
                content=table,
                padding=10,
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.GREY_300),
            ),
            ft.Text(f"စုစုပေါင်း {len(data.offers)} ခု", size=14, color=ft.colors.GREY_600),
        )

    except Exception as e:
        # ဘယ်လို error မဆို blank မဖြစ်အောင်
        error_text = traceback.format_exc()
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("❌ Application Error", size=24, color=ft.colors.RED_700),
                    ft.Text("ကျေးဇူးပြုပြီး အမှားအကြောင်းကို အောက်ပါအတိုင်း Developer ကို ပြန်ပြောပါ။", size=16),
                    ft.Text(error_text, size=12, color=ft.colors.RED_500, selectable=True),
                ]),
                padding=20,
                bgcolor=ft.colors.RED_50,
                border_radius=10,
            )
        )

ft.app(target=main)
