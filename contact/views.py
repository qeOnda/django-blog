from django.shortcuts import render
from django.shortcuts import redirect


from .forms import ContactForm
from posts.models import Post

def contact_view(requests):
	footer = Post.objects.order_by('-time_stamp')[0:2]
	form = ContactForm()
	if requests.method == 'POST':
		form = ContactForm(requests.POST)
		if form.is_valid():
			form.save()
			return redirect('contact-us')
	context = {
		'footer': footer,
		'form': form
	}
	return render(requests, 'contact.html', context)	