import flet as ft
import json
import os
import sys

def main(page: ft.Page):
    page.title = "Barmill Offer"
    page.padding = 20
    
    # ListView သုံးခြင်းဖြင့် Error တက်ရင်လည်း မျက်နှာပြင်ပေါ် စာသား ပေါ်လာမည်
    list_view = ft.ListView(expand=True, spacing=10)
    page.add(list_view)
    
    # --- [အရေးကြီးဆုံးအပိုင်း] APK ထဲတွင် Assets လမ်းကြောင်း မှန်ကန်စွာ ရှာဖွေခြင်း ---
    # local run ရင် လက်ရှိ ပတ်လမ်းကြောင်း၊ APK ဆောက်ရင် ၎င်း App ရဲ့ internal path ကို ယူမည်
    base_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_path, "assets", "data.json")
    
    # ဒုတိယနည်းလမ်းဖြင့် ထပ်မံစစ်ဆေးခြင်း
    if not os.path.exists(json_path):
        json_path = os.path.join("assets", "data.json")

    # အကယ်၍ မတွေ့သေးပါက
    if not os.path.exists(json_path):
        list_view.controls.append(
            ft.Text(f"❌ ရှာမတွေ့ပါ! လမ်းကြောင်း: {os.path.abspath(json_path)}", size=16, color=ft.colors.RED)
        )
        page.update()
        return
    
    # 2. JSON ဖိုင်ကိုဖတ်မယ်
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            offers = json.load(f)
    except Exception as e:
        list_view.controls.append(
            ft.Text(f"❌ ဒေတာဖတ်ရန် Error တက်နေသည်: {e}", size=16, color=ft.colors.RED)
        )
        page.update()
        return
    
    # 3. ဒေတာမရှိရင်
    if not offers:
        list_view.controls.append(
            ft.Text("⚠️ data.json ထဲတွင် မည်သည့်ဒေတာမှ မရှိပါ", size=18, color=ft.colors.ORANGE)
        )
        page.update()
        return
    
    # 4. ဒေတာပြမယ်
    list_view.controls.append(
        ft.Text(f"✅ ဒေတာ အောင်မြင်စွာ ဖတ်ပြီးပါပြီ ({len(offers)} items)", size=18, color=ft.colors.GREEN)
    )
    list_view.controls.append(ft.Divider(height=10))
    
    # ပထမဆုံး 5 ခုကိုပြမယ် (စမ်းသပ်ရန်)
    for item in offers[:5]:
        list_view.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"No: {item.get('No.', '')}", weight="bold"),
                        ft.Text(f"Item: {item.get('Item', '')}"),
                        ft.Text(f"Code: {item.get('Code', '')}"),
                        ft.Text(f"Price: {item.get('Unit Price (USD)', '')}"),
                    ]),
                    padding=15,
                ),
                elevation=3,
                margin=5,
            )
        )
    
    list_view.controls.append(ft.Text(f"Total: {len(offers)} items", size=14, color=ft.colors.GREY))
    page.update()

# assets_dir ဖော်ပြပေးရန် အထူးလိုအပ်သည်
ft.app(target=main, assets_dir="assets")
