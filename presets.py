PRESET_PROMPTS = {
    "Default Assistant": "You are a helpful, professional AI assistant.",
    "Code Expert": "You are an expert software developer...",
    # others...
}

def get_prompt(preset_name):
    return PRESET_PROMPTS.get(preset_name, PRESET_PROMPTS["Default Assistant"])
