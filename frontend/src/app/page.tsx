export default async function Home() {
  const res = await fetch("http://backend:8000/api/posts/");
  const posts = await res.json();
  const resHello = await fetch("http://backend:8000/api/hellos/");
  const hellos = await resHello.json();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      {posts.map((post: any) => (
        <div key={post.id}>
          <h1>{post.title}</h1>
          <h2>{post.description}</h2>
        </div>
      ))}

      {hellos.map((hello: any) => (
        <div className="" key={hello.id}>
          <h1>
            {hello.firstname} - {hello.lastname}
          </h1>
        </div>
      ))}
    </main>
  );
}
