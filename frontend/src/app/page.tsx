export default async function Home() {
  const res = await fetch("http://backend:8000/api/posts/");
  const posts = await res.json();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      {posts.map((post: any) => (
        <div key={post.id}>
          <h1>{post.title}</h1>
          <h2>{post.description}</h2>
        </div>
      ))}
    </main>
  );
}
