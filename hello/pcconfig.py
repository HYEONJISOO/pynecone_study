import pynecone as pc


config = pc.Config(
    app_name="hello",
    # bunpath 왜 없지? 디폴트라그랬는데? 나 번도 깔았을텐데?
    # bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
