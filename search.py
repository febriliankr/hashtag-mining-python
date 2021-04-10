import twint
# configuration
config = twint.Config()
config.Search = "bitcoin"
config.Lang = "en"
config.Limit = 100
# config.Since = "2020–04–04 16:48:36"
# config.Until = "2021–04–04 16:48:36"
config.Store_json = True
config.Output = "custom_out.json"
# running search
twint.run.Search(config)
